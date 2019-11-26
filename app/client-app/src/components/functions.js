async function loadGenes(page) {
    var page_number = encodeURIComponent(page)
    var url = new URL("http://localhost:5000/gene"),
        params = {
            "page": page_number
        }
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))

    let response = await fetch(url, {
        mode: 'cors',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then((res) => (res.json())).then((res) => (res["Entities"]));

    return response;
}

async function loadDiseases(page) {
    var page_number = encodeURIComponent(page)
    var url = new URL("http://localhost:5000/disease"),
        params = {
            "page": page_number
        }
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))

    let response = await fetch(url, {
        mode: 'cors',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then((res) => (res.json())).then((res) => (res["Entities"]));

    return response;
}

async function loadGeneInfo(geneName) {
    var url = new URL("http://localhost:5000/gene/" + geneName)
    let response = await fetch(url, {
        mode: 'cors',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then((res) => (res.json()));

    return response;
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

export { loadDiseaseInfo, loadGeneInfo, loadGenes, loadDiseases };