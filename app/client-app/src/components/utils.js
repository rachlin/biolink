import React from 'react';
import { Link } from 'react-router-dom';

import schema from './schema.js';

// This orders the columns placing important ones at the front based on the schema
// allows geneId/diseaseId/geneName/diseaseName to be the first two columns of the table
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

export { sortProperties, convertNameToLink };