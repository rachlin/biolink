import React, { Component } from 'react'
import ReactSearchBox from 'react-search-box'
import { Switch, Route, Redirect } from "react-router-dom";

export default class Search extends Component {
  data = [
    {
      key: 'john',
      value: 'John Doe',
      link: "/gene/NAT2",
    },
    {
      key: 'jane',
      value: 'Jane Doe',
    },
    {
      key: 'mary',
      value: 'Mary Phillips',
    },
    {
      key: 'robert',
      value: 'Robert',
    },
    {
      key: 'karius',
      value: 'Karius',
    },
  ]

  redirect(record) {
      return (
        <Switch>
            <Route>
                <Redirect push to="/gene/NOS2" />
            </Route>
        </Switch>
      );
  };

  render() {
    return (
      <ReactSearchBox
        placeholder="Placeholder"
        value="Doe"
        data={this.data}
        callback={record => console.log(record)}
        // onSelect={}
        onSelect={record => this.redirect(record)}
      />
    )
  }
}