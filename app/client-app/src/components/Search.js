import React, { useState, useEffect } from 'react';
import { Switch, Route, Redirect } from "react-router-dom";

import Gene from "./Gene";
import { loadGeneInfo } from "./functions.js";
import { stringify } from 'querystring';

export default function Search() {
    const [searchValue, setSearchValue] = useState("");
    const [genes, setGenes] = useState([]);
    const [diseases, setDiseases] = useState([]);

    // useEffect(() => {
    //     async function fetchData() {
    //       const response = await loadGenes(page);
    //       setGenes(genes.concat(response));
    //       setGeneData(
    //         gene_data.concat(
    //           response.map((geneName) => (
    //             {
    //               geneName: geneName
    //             }))));
    //     }
    //     fetchData();
    //   }, [page]);
    
    

    function redirect (record) {
        console.log(record)
        setSearchValue(record)
        return <Gene />;
    };

    function filter(value) {   
    }

    return (
        <div>Search here</div>
        
    )
}