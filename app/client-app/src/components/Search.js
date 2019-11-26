import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';

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

  return (
    <div>
        <form className={classes.root} noValidate autoComplete="off">
        <TextField id="standard-basic" label="Standard" />
        </form>
        <div className={classes.root}>
            <Button variant="contained">Search</Button>
        </div>
    </div>
  );
}