import React from "react";
import { Navbar } from "react-bootstrap";

const Header = ({ title }) => {
  // const Header = (props) => {
  // const {title} = props;
  return (
    <Navbar bg="light" variant="light">
      {/* <Container> */}
      <Navbar.Brand href="/">{title}</Navbar.Brand>
      {/* <Navbar.Brand href="/">{props.title}</Navbar.Brand> */}
      {/* </Container> */}
    </Navbar>
  );
};

export default Header;
