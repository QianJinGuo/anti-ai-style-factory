FROM nginx:alpine

# Copy gallery (static site)
COPY gallery/ /usr/share/nginx/html/gallery/

# Copy sample styles and symlink as styles/ (gallery expects ../styles/)
COPY sample_styles/ /usr/share/nginx/html/styles/

# Copy demos
COPY demos/ /usr/share/nginx/html/demos/

# Root index: redirect to gallery
RUN echo '<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0;url=/gallery/"></head></html>' \
    > /usr/share/nginx/html/index.html

# nginx config: enable SPA-like routing, CORS for local dev
RUN cat > /etc/nginx/conf.d/default.conf <<'NGINX'
server {
    listen 80;
    server_name _;
    root /usr/share/nginx/html;
    index index.html;

    # CORS for local development
    add_header Access-Control-Allow-Origin *;

    # Gallery
    location /gallery/ {
        try_files $uri $uri/ /gallery/index.html;
    }

    # Styles (sample_styles mapped as /styles/)
    location /styles/ {
        autoindex on;
    }

    # Demos
    location /demos/ {
        autoindex on;
    }

    # Health check
    location /health {
        return 200 'ok';
        add_header Content-Type text/plain;
    }
}
NGINX

EXPOSE 80
