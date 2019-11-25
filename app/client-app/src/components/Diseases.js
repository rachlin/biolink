import React, {useState, useEffect} from 'react';
import { Switch, Route, Link, useRouteMatch } from "react-router-dom";

import Disease from './Disease';


export default function Diseases() {
    let match = useRouteMatch();
  
    const [page, setPage] = useState(0);
    const [diseases, setDiseases] = useState([]);
  
    useEffect(() => {
      async function fetchData() {
        const response = await loadDiseases(page);
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
              <Link to={`/disease/${diseaseName}`}>{diseaseName}</Link>
            </li>
          ))}
        </ul>
  
        <button onClick={() => setPage(page + 1)}> Load more diseases </button>
  
        <Switch>
          <Route path={match.path}>
            <h3>Please select a disease.</h3>
          </Route>
        </Switch>
      </div>
    );
  }

  async function loadDiseases(page) {
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