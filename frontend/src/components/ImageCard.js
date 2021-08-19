import React from 'react';
import { Card, Button } from 'react-bootstrap';

const ImageCard = () => {
  return (
    <Card style={{ width: '18rem' }}>
      <Card.Img
        variant="top"
        src="https://images.unsplash.com/photo-1503736334956-4c8f8e92946d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwyNTM3MjN8MHwxfHJhbmRvbXx8fHx8fHx8fDE2MjkzOTg0MjE&ixlib=rb-1.2.1&q=80&w=400"
      />
      <Card.Body>
        <Card.Title>Card Title</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </Card.Text>
        <Button variant="primary">Go somewhere</Button>
      </Card.Body>
    </Card>
  );
};

export default ImageCard;
