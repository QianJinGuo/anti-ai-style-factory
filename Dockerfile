FROM openresty/openresty:alpine

RUN apk add --no-cache curl lua-resty-http

# Copy lua-resty-http to openresty's LuaJIT path
RUN mkdir -p /usr/local/openresty/site/lualib/resty && \
    cp /usr/share/lua/common/resty/*.lua /usr/local/openresty/site/lualib/resty/

# Copy gallery (static site)
COPY gallery/ /usr/share/nginx/html/gallery/

# Copy sample styles (gallery expects /styles/)
COPY sample_styles/ /usr/share/nginx/html/styles/

# Copy demos
COPY demos/ /usr/share/nginx/html/demos/

# Root index: redirect to gallery
RUN echo '<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0;url=/gallery/"></head></html>' \
    > /usr/share/nginx/html/index.html

# nginx + Lua config
RUN cat > /usr/local/openresty/nginx/conf/nginx.conf <<'NGINX'
worker_processes 1;
events { worker_connections 1024; }
http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile      on;
    keepalive_timeout 65;
    resolver 127.0.0.11 ipv6=off;

    server {
        listen 80;
        server_name _;
        root /usr/share/nginx/html;
        index index.html;

        add_header Access-Control-Allow-Origin *;

        location /gallery/ {
            try_files $uri $uri/ /gallery/index.html;
        }

        location /styles/ {
            autoindex on;
        }

        location /demos/ {
            autoindex on;
        }

        # URL proxy for scorer — fetches external HTML and returns it
        location = /proxy {
            default_type text/html;
            charset utf-8;
            content_by_lua_block {
                local url = ngx.var.arg_url
                if not url or url == "" then
                    ngx.status = 400
                    ngx.say("Missing ?url= parameter")
                    return
                end
                local httpc = require("resty.http").new()
                httpc:set_timeout(10000)
                local res, err = httpc:request_uri(url, {
                    method = "GET",
                    ssl_verify = false,
                    headers = {
                        ["User-Agent"] = "Mozilla/5.0 (compatible; AntiAI-Scorer/1.0)"
                    }
                })
                if not res then
                    ngx.status = 502
                    ngx.say("Fetch failed: " .. (err or "unknown error"))
                    return
                end
                ngx.say(res.body)
            }
        }

        location /health {
            return 200 'ok';
            add_header Content-Type text/plain;
        }
    }
}
NGINX

EXPOSE 80
