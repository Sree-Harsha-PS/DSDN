import React, { useState, useEffect } from 'react';
import axios from 'axios';
import * as d3 from 'd3';
import Header from '../../layout/users/Header';
import Footer from '../../layout/pages/Footer';
import Card from '../../components/Card'; // Assuming you have a Card component
import cardsData from '../../assets/Features'; // Assuming you have card data

const NodeViz = () => {
  const [nodes, setNodes] = useState([]);

  useEffect(() => {
    // Fetch nodes from Flask backend
    const fetchNodes = async () => {
      try {
        const response = await axios.get('/api/nodes'); // Assuming your Flask API endpoint is '/api/nodes'
        setNodes(response.data.nodes);
      } catch (error) {
        console.error('Error fetching nodes:', error);
      }
    };

    fetchNodes();
  }, []); // Run only once on component mount

  useEffect(() => {
    // D3.js code for visualization
    if (nodes.length > 0) {
      // Clear previous visualization if any
      d3.select('#node-viz').selectAll('*').remove();

      // Create SVG container
      const svg = d3.select('#node-viz')
        .append('svg')
        .attr('width', 800)
        .attr('height', 600);

      // Your D3 visualization code here
      // Example: render circles for each node
      svg.selectAll('circle')
        .data(nodes)
        .enter()
        .append('circle')
        .attr('cx', (d, i) => i * 50)
        .attr('cy', 100)
        .attr('r', 20)
        .style('fill', 'blue');
    }
  }, [nodes]); // Re-run whenever nodes change

  return (
    <div className="page-view">
      <div className="content page-view">
        <Header />
        <div className="card-container">
          {cardsData.map((card, index) => (
            <Card key={index} title={card.title} features={card.features} />
          ))}
        </div>
        <div id="node-viz"></div> {/* Visualization container */}
        <Footer />
      </div>
    </div>
  );
};

export default NodeViz;
