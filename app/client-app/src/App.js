import React, {useState, useEffect} from 'react';
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
          <li>
            <Link to="/disease">Diseases</Link>
          </li>
        </ul>

        <Switch>
          <Route path="/about">
            <About />
          </Route>
          <Route path="/gene">
            <Genes />
          </Route>
          <Route path="/disease">
            <Diseases />
          </Route>
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

  const [page, setPage] = useState(0);
  const [genes, setGenes] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await loadGenes(page);
      setGenes(genes.concat(response));
    }
    fetchData();
  }, [page]);

  return (
    <div>
      <h2>Genes</h2>

      <ul>
        {genes && genes.map((geneName) => (
          <li>
            <Link to={`${match.url}/${geneName}`}>{geneName}</Link>
          </li>
        ))}
      </ul>

      <button onClick={() => setPage(page + 1)}> Load more genes </button>

      <Switch>
        <Route path={`${match.path}/:geneName`}>
          <Gene />
        </Route>
        <Route path={match.path}>
          <h3>Please select a gene.</h3>
        </Route>
      </Switch>
    </div>
  );
}


function Diseases() {
  let match = useRouteMatch();

  const [page, setPage] = useState(0);
  const [diseases, setDiseases] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await loadDisease(page);
      setDiseases(diseases.concat(response));
    }
    fetchData();
  }, [page]);

  return (
    <div>
      <h2>Diseases</h2>

      <ul>
        {diseases && diseases.map((diseaseName) => (
          <li>
            <Link to={`${match.url}/${diseaseName}`}>{diseaseName}</Link>
          </li>
        ))}
      </ul>

      <button onClick={() => setPage(page + 1)}> Load more diseases </button>

      <Switch>
        <Route path={`${match.path}/:diseaseName`}>
          {/* <Disease /> */}
        </Route>
        <Route path={match.path}>
          <h3>Please select a disease.</h3>
        </Route>
      </Switch>
    </div>
  );
}


function Gene() {
  let { geneName } = useParams();
  let match = useRouteMatch();

  const [data, setData] = useState({});

  useEffect(() => {
    async function fetchData() {
      const response = await loadGeneInfo(geneName);
      console.log(response)
      setData(response);
    }
    fetchData();
  }, [geneName]);
  

  var related = Object.assign({}, data.Neighbors)
  var diseases = [].concat(related.Disease)
  related = Object.assign({}, data.RelatedGenes)
  var genes = [].concat(related.RelatedByDisease)


  return (
    <div>
      <center><h1>Gene Details</h1></center>
      <div>
        Associated Diseases
        <ul>
          {diseases.map((disease) => (
            <li><Link to="/disease/:disease">{disease}</Link></li>
          ))}
        </ul>
      </div>
      <div>
        Related Genes by Disease Association
        <ul>
          {genes.map((gene) => (
            <li><Link to="/gene/:gene">{gene}</Link></li>
          ))}
        </ul>
      </div>
    </div>
  )
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
  }).then((res) => (res.json())).then((res) => (res["Genes"]));

  return response;
}

async function loadGeneInfo(geneName) {
  var url = new URL("http://localhost:5000/gene/" + geneName)
  let response = await fetch(url, {
    mode: 'cors',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json'
    }
  }).then((res) => (res.json()));

  return response;
}

async function loadDisease(page) {
  var page_number = encodeURIComponent(page)
  var url = new URL("http://localhost:5000/disease"),
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
  }).then((res) => (res.json())).then((res) => (res["Diseases"]));

  return response;
}