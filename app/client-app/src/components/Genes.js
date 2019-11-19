import React, {useState, useEffect} from 'react';
import { Switch, Route, Link, useRouteMatch } from "react-router-dom";

import Gene from './Gene';


export default function Genes() {
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
              <Link to={`/gene/${geneName}`}>{geneName}</Link>
            </li>
          ))}
        </ul>
  
        <button onClick={() => setPage(page + 1)}> Load more genes </button>
  
        <Switch>
          <Route path={`/gene/:geneName`}>
            <Gene />
          </Route>
          <Route path={match.path}>
            <h3>Please select a gene.</h3>
          </Route>
        </Switch>
      </div>
    );
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