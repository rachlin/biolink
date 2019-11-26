import React, { useState, useEffect } from 'react';

import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import SimpleTable from './Table';


import { loadSearchResults } from './functions.js';
import { sortProperties, convertNameToLink } from './utils.js';

const useStyles = makeStyles(theme => ({
  root: {
    '& > *': {
      margin: theme.spacing(1),
      width: 200,
    },
  },
}));

export default function Search() {
  const classes = useStyles();

  const [searchVal, setSearchVal] = useState("")
  const [results, setResults] = useState({})
  const [resKeys, setResKeys] = useState([])


  useEffect(() => {
    async function fetchData() {
      if (searchVal.length >= 3) {
        const response = await loadSearchResults(searchVal);
        setResults(response);
        setResKeys(Object.keys(response));
      }
    }
    fetchData();
  }, [searchVal]);

  return (
    <div>
        <form className={classes.root} noValidate autoComplete="off">
            <TextField id="standard-basic" label="Standard" value={searchVal} onChange={(event) => setSearchVal(event.target.value)}/>
        </form>

        {resKeys.map((key) => {
            var result_ent = results[key]["Entities"]
            if (result_ent.length > 0) {
                var props = Object.keys(result_ent[0]);
                props = sortProperties(props, key.toLowerCase())

                return <SimpleTable cols={props} rows={convertNameToLink(result_ent, key.toLowerCase())} />;
            }
        })}

        {console.log(results)}
        

    </div>
  );
}