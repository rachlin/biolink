import React, { useState, useEffect } from 'react';
import { Link, useRouteMatch, useParams } from "react-router-dom";

export default function Disease() {
    let { diseaseName } = useParams();
    let match = useRouteMatch();
  
    const [data, setData] = useState({});
  
    useEffect(() => {
      async function fetchData() {
        const response = await loadDiseaseInfo(diseaseName);
        console.log(response)
        setData(response);
      }
      fetchData();
    }, [diseaseName]);
    
  
    var related = Object.assign({}, data.Neighbors)
    var genes = [].concat(related.Gene)
    related = Object.assign({}, data.RelatedDiseases)
    var diseases = [].concat(related.RelatedByGene)
  
  
    return (
      <div>
        <center><h1>Disease Details</h1></center>
        <div>
          Associated Genes
          <ul>
            {genes.map((gene) => (
              <li><Link to={`/gene/${gene}`}>{gene}</Link></li>
            ))}
          </ul>
        </div>
        <div>
          Related Diseases by Gene Association
          <ul>
            {diseases.map((disease) => (
              <li><Link to={`/disease/${disease}`}>{disease}</Link></li>
            ))}
          </ul>
        </div>
      </div>
    )
  }
  
  async function loadDiseaseInfo(diseaseName) {
    var url = new URL("http://localhost:5000/disease/" + diseaseName)
    let response = await fetch(url, {
      mode: 'cors',
      credentials: 'same-origin',
      headers: {
        'Content-Type': 'application/json'
      }
    }).then((res) => (res.json()));
  
    return response;
  }