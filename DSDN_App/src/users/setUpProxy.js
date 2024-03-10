// src/setupProxy.js
const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    createProxyMiddleware('/api', {
      target: 'http://127.0.1.1:3000', // Change this to your backend server URL
      changeOrigin: true,
      onProxyRes: function(proxyRes, req, res) {
        // Allow CORS for all domains
        proxyRes.headers['Access-Control-Allow-Origin'] = '*';
      },
    })
  );
};
