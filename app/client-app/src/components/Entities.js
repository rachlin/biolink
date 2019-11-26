import React, { useState, useEffect } from 'react';

import SimpleTable from './Table';
import { loadEntities } from './functions.js';
import { sortProperties, convertNameToLink } from './utils.js';

function Entities(props) {
  let title = props.title;
  let entityType = props.entityType;

  const [page, setPage] = useState(0);
  const [entities, setEntities] = useState([]);
  const [properties, setProperties] = useState([]);


  useEffect(() => {
    async function fetchData() {
      const response = await loadEntities(entityType, page);
      const newEntities = entities.concat(response);
      setEntities(newEntities);
      if (newEntities.length > 0) {
        const unorderedProps = Object.keys(newEntities[0]);
        const orderedProps = sortProperties(unorderedProps, entityType);
        setProperties(orderedProps);
      }
    }
    fetchData();
  }, [page]);

  return (
    <div>
      <h2>{title}</h2>

      <SimpleTable cols={properties} rows={convertNameToLink(entities, entityType)} />
      <button onClick={() => setPage(page + 1)}> Load more .. </button>

    </div>
  );
}

const Genes = () => (<Entities title="Genes" entityType="gene"/>)
const Diseases = () => (<Entities title="Diseases" entityType="disease"/>)

export { Genes, Diseases }
