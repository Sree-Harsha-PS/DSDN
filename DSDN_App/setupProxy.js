const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: 'http://127.0.1.1:5000', // Change this to your Flask backend URL
      changeOrigin: true,
      headers: {
        'Access-Control-Allow-Origin': 'http://localhost:3000', // Change this to your React frontend URL
        'Access-Control-Allow-Credentials': 'true',
      },
    })
  );
};
