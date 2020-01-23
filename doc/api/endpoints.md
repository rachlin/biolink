## API Endpoints

(As of 12/9/19, we have not yet deployed the API. We refer to API usage strictly locally.)

Users can access the API directly by making HTTP Requests to different endpoints.

**Get All Nodes of Same Type**
----
Returns the first 25 entities of a given type. If a page number is provided, returns the 25 entries beginning at page_number * 25.

* **URL**

  /gene
  /disease

* **Method:**

  `GET`
  
*  **URL Params**

   **Optional:**
 
   `page=[integer]`, (will be 0 by default)

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 

        {
            "Entities": [{} .....],
            "Page": 0
        }
 
* **Error Response:**

  * **Code:** 200 <br />
    **Content:** `{}`
    **Case:**: Occurs when node type doesn't exist

  OR

  * **Code:** 200 <br />
    **Content:**

        {
            "Entities": [],
            "Page": 100000
        }
    **Case:**: Occurs when page number does not exist

* **Sample Call:**

  `curl -X GET "localhost:5000/gene?page=0"`
  `curl -X GET "localhost:5000/gene"`
  `curl -X GET "localhost:5000/disease?page=10"`
  `curl -X GET "localhost:5000/disease"`

**Get Specific Node Details**
----
Returns information about a specific node.

* **URL**

  /gene/:geneSymbol
  /disease/:diseaseName

* **Method:**

  `GET`

* **Success Responses:**

  * **Code:** 200 <br />
    **Content:** 

        {
            "EntityName": "NAT2",
            "Neighbors": {
                "Disease": []
            },
            "RelatedGene": {
                "RelatedByDisease": []
            }
        }

  * **Code:** 200 <br />
    **Content:** 

        {
            "EntityName": "Asthma",
            "Neighbors": {
                "Gene": []
            },
            "RelatedDisease": {
                "RelatedByGene": []
            }
        }
 
* **Error Response:**

  * **Code:** 200 <br />
    **Content:** 

        {
            "EntityName": "fakeGeneSymbol",
            "Neighbors": {
                "Disease": []
            },
            "RelatedGene": {
                "RelatedByDisease": []
            }
        }
    **Case**: Occurs when the gene does not exist.

  * **Code:** 200 <br />
    **Content:** 

        {
            "EntityName": "fakeDiseaseName",
            "Neighbors": {
                "Gene": []
            },
            "RelatedDisease": {
                "RelatedByGene": []
            }
        }
    **Case**: Occurs when the disease does not exist.
    

* **Sample Call:**

  `curl -X GET "localhost:5000/gene/NAT2"`
  `curl -X GET "localhost:5000/disease/Asthma"`


  **Search across all node types**
----
Returns information about nodes that have a property that matches searched value.

* **URL**

  /search

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**

   `nodeVal:[alphanumberic]`

<!-- * **Data Params**

  <_If making a post request, what should the body payload look like? URL Params rules apply here too._> -->

* **Success Responses:**

  * **Code:** 200 <br />
    **Content:** 

        {
            "Disease": {
                "Entities": [...]
            },
            "Gene": {
                "Entities": [...]
            }
        }

* **Error Response:**

  * **Code:** 200 <br />
    **Content:** 

        {
            "Disease": {
                "Entities": []
            },
            "Gene": {
                "Entities": []
            }
        }
    **Case**: Occurs when the no node exists that has properties matching the search parameter.
    

* **Sample Call:**

  `curl -X GET "localhost:5000/search?nodeVal=Asth"`
  `curl -X GET "localhost:5000/search?nodeVal=NOS"`