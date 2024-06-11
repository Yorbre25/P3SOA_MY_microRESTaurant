# Use the official Nginx image as the base image
FROM nginx:latest

# Copy the built Angular application to the Nginx default public directory
COPY dist/my-rest-aurant/browser /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx when the Docker container starts
CMD ["nginx", "-g", "daemon off;"]