import React from "react";
import { Col, Container, Form, Row, Button } from "react-bootstrap";

const Search = () => {
  return (
    <Container>
      <Row>
        <Col>
          <Form>
            <Form.Row>
              <Col>
                <Form.Control placeholder="Search for new image" />
              </Col>
              <Col>
                <Button variant="primary" type="submit">
                  Search
                </Button>
              </Col>
            </Form.Row>
          </Form>
        </Col>
      </Row>
    </Container>
  );
};

export default Search;
