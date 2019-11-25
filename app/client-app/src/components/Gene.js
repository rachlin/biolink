import React, { useState, useEffect } from 'react';
import { Link, useParams } from "react-router-dom";

import { loadGeneInfo } from './functions.js';

export default function Gene() {
    let { geneName } = useParams();

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
                        <li><Link to={`/disease/${disease}`}>{disease}</Link></li>
                    ))}
                </ul>
            </div>
            <div>
                Related Genes by Disease Association
                <ul>
                    {genes.map((gene) => (
                        <li><Link to={`/gene/${gene}`}>{gene}</Link></li>
                    ))}
                </ul>
            </div>
        </div>
    )
}