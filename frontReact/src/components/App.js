import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("api/vulnerability")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
      <table>
        {this.state.data.map(vulnerability => {
          return (
            <tr key={vulnerability.id} style="border: 1px solid black;">
              <td>{vulnerability.asset_hostname}</td>
              <td>{vulnerability.asset_ip_address}</td>
              <td>{vulnerability.vulnerability_title}</td>
              <td>{vulnerability.vulnerability_severity}</td>
              <td>{vulnerability.vulnerability_cvss}</td>
              <td>{vulnerability.vulnerability_publication_date}</td>
            </tr>
          );
        })}
      </table>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);