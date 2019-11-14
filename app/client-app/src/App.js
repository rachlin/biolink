import React from 'react';
import logo from './logo.svg';
// import Gene from './components/gene';
// import Disease from './components/disease';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link, useRouteMatch, useParams } from "react-router-dom";


let state = {
  genes: ['IL4', 'NOS2', 'ILI3']
}

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
  loadGeneAsync(page);

  return (
    <div>
      <h2>Genes</h2>

      <ul>
        {state.genes && state.genes.map((geneName) => (
          <li>
            <Link to={`${match.url}/${geneName}`}>{geneName}</Link>
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
          loadGeneAsync(page)
        </Route>
        <Route path={match.path}>
          <h3>Please select a gene.</h3>
        </Route>
      </Switch>
    </div>
  );
}


function Gene() {
  let { geneName } = useParams();

  var url = new URL("http://localhost:5000/gene/" + geneName)
  var gene_md = fetch(url, {
    mode: 'cors',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json'
    }
  });

  var diseases = [].concat(gene_md.AssociatedDiseases)

  var related = Object.assign({}, gene_md.RelatedGenes)
  var genes = [].concat(related.RelatedByDisease)


  return (
    <div>
      <center><h1>Gene {geneName} Details</h1></center>
      <div>
        Associated Diseases
        <ul>
          {diseases.map((disease) => (
            <li><a href={link("disease", disease)}>{disease}</a></li>
          ))}
        </ul>
      </div>
      <div>
        Related Genes by Disease Association
                <ul>
          {genes.map((gene) => (
            <li><a href={link("gene", gene)}>{gene}</a></li>
          ))}
        </ul>
      </div>
    </div>
  )
}

function link(type, node_name) {
  return '/'+ type + '/' + node_name
}


async function loadGenes(page) {
  var page_number = encodeURIComponent(page)
  var url = new URL("http://localhost:5000/gene"),
    params = {
      "page": page_number
    }
  Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))

  let response = await fetch(url, {
    mode: 'cors',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json'
    }
  });
  response = response.json()
  response = response["Genes"]

  return response;
}


function loadGeneAsync(page) {
  if (page === 0) {
    console.log("hi")
    loadGenes(page).then(response => (state.genes = response))
  } else {
    loadGenes(page).then(response => (state.genes.concat(response)))
  }
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

// function Disease() {
//   let { diseaseName } = useParams();

//   return <h3>Requested disease name: {diseaseName}</h3>;
// }