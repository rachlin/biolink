import React, {useState, useEffect, useMemo} from 'react';
import { Switch, Route, Link, useRouteMatch } from "react-router-dom";

import { loadGenes } from './functions.js';
import SimpleTable from './Table';

export default function Genes() {
    let match = useRouteMatch();
  
    const [page, setPage] = useState(0);
    const [genes, setGenes] = useState([]);
    const [columns, setColumns] = useState([]);

  
    useEffect(() => {
      async function fetchData() {
        const response = await loadGenes(page);
        setGenes(genes.concat(response));
        if (genes.length > 0) {
          setColumns(Object.keys(genes[0]));
        }
      }
      fetchData();
    }, [page]);
  
    return (
      <div>
        <h2>Genes</h2>
  
        {/* <ul>
          {genes && genes.map((geneName) => (
            <li>
              <Link to={`/gene/${geneName}`}>{geneName}</Link>
            </li>
          ))}
        </ul> */}
        {console.log(columns) && <SimpleTable columns={columns} rows={genes} />}

        <button onClick={() => setPage(page + 1)}> Load more genes </button>
  
        <Switch>
          <Route path={match.path}>
            <h3>Please select a gene.</h3>
          </Route>
        </Switch>
      </div>
    );
  }