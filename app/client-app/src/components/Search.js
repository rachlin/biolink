import React, { useState, useEffect } from 'react';
import SearchBar from 'material-ui-search-bar'
import { Switch, Route, Redirect } from "react-router-dom";

export default function Search() {
    const [searchValue, setSearchValue] = useState("");
    const [genes, setGenes] = useState([]);
    const [diseases, setDiseases] = useState([]);

    const data = ["Hi", "bye"]

    function redirect (record) {
        return (
            <Switch>
                <Route>
                    <Redirect push to="/gene/NOS2" />
                </Route>
            </Switch>
        );
    };

    function filter(value) {

    }

    return (
        <SearchBar
            value={searchValue}
            onChange={(newValue) => setSearchValue(newValue)}
            // onRequestSearch={() => console.log(searchValue)}
            onRequestSearch={() => redirect(searchValue)}
            onCancelSearch={() => setSearchValue("")}
            style={{
                margin: '0 auto',
                maxWidth: 800
            }}
            dataSource={data}
        />
    )
}