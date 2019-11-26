import React, {useState, useEffect, useMemo} from 'react';
import { Switch, Route, Link, useRouteMatch } from "react-router-dom";

import { loadGenes } from './functions.js';
import SimpleTable from './Table';

export default function Genes() {
    let match = useRouteMatch();
  
    const [page, setPage] = useState(0);
    const [genes, setGenes] = useState([]);
    const [properties, setProperties] = useState([]);

  
    useEffect(() => {
      async function fetchData() {
        const response = await loadGenes(page);
        const newGenes = genes.concat(response);
        setGenes(newGenes);
        if (newGenes.length > 0) {
          setProperties(Object.keys(newGenes[0]));
        }
      }
      fetchData();
    }, [page]);
  
    return (
      <div>
        <h2>Genes</h2>
        
        <SimpleTable cols={properties} rows={genes} />

        <button onClick={() => setPage(page + 1)}> Load more genes </button>
  
        <Switch>
          <Route path={match.path}>
            <h3>Please select a gene.</h3>
          </Route>
        </Switch>
      </div>
    );
  }