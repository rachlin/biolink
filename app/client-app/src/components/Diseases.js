import React, { useState, useEffect } from 'react';
import { Switch, Route, Link, useRouteMatch } from "react-router-dom";

import { loadDiseases } from './functions.js';

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