import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

import { loadEntities } from './functions.js';
import schema from './schema.js';

import SimpleTable from './Table';

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


function sortProperties(properties, entityType) {
  var ordered = [].concat(properties)

  schema.forEach((schema_def) => {
    if (schema_def.entityType === entityType) {
      schema_def.propertiesOfImportance.forEach((impProp) => {
        var ind = ordered.indexOf(impProp)
        ordered.splice(ind, 1)
        ordered.unshift(impProp);
      });    
      }
    });  

  return ordered
}

function convertNameToLink(items, entityType) {
  schema.forEach((schema_def) => {
    if (schema_def.entityType === entityType) {
      items.forEach((item) => {
        item[schema_def.nameKey] = (<Link to={`/${entityType}/${ item[schema_def.nameKey]}`}>{ item[schema_def.nameKey]}</Link>)
      })
    }
  })
  return items
}

const Genes = () => (<Entities title="Genes" entityType="gene"/>)
const Diseases = () => (<Entities title="Diseases" entityType="disease"/>)

export { Genes, Diseases }
