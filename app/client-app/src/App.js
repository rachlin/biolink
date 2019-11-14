import React from 'react';
import logo from './logo.svg';
// import Gene from './components/gene';
// import Disease from './components/disease';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link, useRouteMatch, useParams } from "react-router-dom";

export default function App() {
  return (
    <Router>
      <div>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/about">About</Link>
          </li>
          <li>
            <Link to="/gene">Genes</Link>
          </li>
          {/* <li>
            <Link to="/disease">Diseases</Link>
          </li> */}
        </ul>

        <Switch>
          <Route path="/about">
            <About />
          </Route>
          <Route path="/gene">
            <Genes />
          </Route>
          {/* <Route path="/disease">
            <Diseases />
          </Route> */}
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}


function Home() {
  return <h2>Home</h2>;
}

function About() {
  return <h2>About</h2>;
}

function Genes() {
  let match = useRouteMatch();

  let page = 0;
  let genes = loadGenes(page)
  console.log(genes)

  return (
    <div>
      <h2>Genes</h2>

      <ul>
        {genes && genes.map((geneName) => (
          <li>
            <Link to={`${match.url}/:geneName`}>{geneName}</Link>
          </li>
        ))}
      </ul>

      <Link to={`${match.url}/load_more`}> Load more genes </Link>

      <Switch>
        <Route path={`${match.path}/:geneName`}>
          <Gene />
        </Route>
        <Route path={`${match.path}/load_more`}>
          page += 1
          genes = loadGenes(page)
        </Route>
        <Route path={match.path}>
          <h3>Please select a gene.</h3>
        </Route>
      </Switch>
    </div>
  );
}

// function Diseases() {
//   let match = useRouteMatch();

//   return (
//     <div>
//       <h2>Diseases</h2>

//       <ul>
//         <li>
//           <Link to={`${match.url}/components`}>Components</Link>
//         </li>
//         <li>
//           <Link to={`${match.url}/props-v-state`}>
//             Props v. State
//             </Link>
//         </li>
//       </ul>

//       <Switch>
//         <Route path={`${match.path}/:diseaseName`}>
//           <Disease />
//         </Route>
//         <Route path={match.path}>
//           <h3>Please select a disease.</h3>
//         </Route>
//       </Switch>
//     </div>
//   );
// }

function Gene() {
  let { geneName } = useParams();

  return <h3>Requested gene name: {geneName}</h3>;
}

// function Disease() {
//   let { diseaseName } = useParams();

//   return <h3>Requested disease name: {diseaseName}</h3>;
// }


function loadGenes(page_number) {
  let jsondata;

  fetch(
    `https://localhost:5000/gene`,
    {
      method: "GET",
      mode: 'cors',
      params : {
        page: page_number
      }
    })
    .then((res) => (res.json()))
    .then(function (res_json) {
      jsondata = res_json;
      // jsondata = [].concat(res_json["Genes"]);
    })
    return jsondata
}