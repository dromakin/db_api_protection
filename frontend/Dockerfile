FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json /app/
RUN npm install
COPY . /app/
ARG FRONTEND_ENV=production
ENV VUE_APP_ENV=${FRONTEND_ENV}
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
#FROM nginx:1.15
COPY --from=0 /app/dist/ /usr/share/nginx/html
#COPY --from=build-stage /nginx.conf /etc/nginx/conf.d/default.conf
#COPY --from=production-stage /nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=0 /app/nginx-backend-not-found.conf /etc/nginx/extra-conf.d/backend-not-found.conf
