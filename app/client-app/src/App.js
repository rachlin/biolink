import React, {Component} from 'react';
import logo from './logo.svg';
import Gene from './components/gene';
import Disease from './components/disease';
import './App.css';

class App extends Component {
  render() {
    if (this.state.type == "") {
      return <div>Hello World</div>
    } else {
      if (this.state.type == "gene") {
        if (this.state.name == "" ) {
          // list all genes with links
          return <div>Hello World</div>
        } else {
          fetch('http://localhost:5000/' + this.state.type + '/' + this.state.name)
          .then(res => res.json())
          .then((data) => {
            this.setState({ data: data })
          }).catch(console.log)

          return (
            <Gene gene={this.state.data} />
          )
        }
      } else if (this.state.type == "disease") {
        if (this.state.name == "" ) {
          // list all diseases with links
          return <div>Hello World</div>
        } else {
          fetch('http://localhost:5000/' + this.state.type + '/' + this.state.name)
          .then(res => res.json())
          .then((data) => {
            this.setState({ data: data })
          }).catch(console.log)

          return (
            <Disease disease={this.state.data} />
          )
        }
      } else {
        return <div>Hello World</div>
      }
    }
  }

  state = {
    type: "gene",
    name: "IL4",
    data: {}
  }

  componentDidMount() {
    fetch('http://localhost:5000/gene/IL4')
    .then(res => res.json())
    .then((data) => {
      this.setState({ gene: data })
    })

    fetch('http://localhost:5000/disease/Asthma')
    .then(res => res.json())
    .then((data) => {
      this.setState({ disease: data })
    })
    .catch(console.log)
  }
}

export default App;
