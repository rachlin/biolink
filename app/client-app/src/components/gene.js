import React from 'react'

const Gene = ({gene}) => {
    
    var diseases = [].concat(gene.AssociatedDiseases)

    var related = Object.assign({}, gene.RelatedGenes)
    var genes = [].concat(related.RelatedByDisease)

    return (
        <div>
            <center><h1>Gene {gene.GeneName} Details</h1></center>
            <div>
                Associated Diseases
                <ul>
                    {diseases.map((disease) => (
                        <li><a href={link("disease", disease)}>{disease}</a></li>
                    ))}
                </ul>
            </div>
            <div>
                Related Genes by Disease Association
                <ul>
                    {genes.map((gene) => (
                        <li><a href={link("gene", gene)}>{gene}</a></li>
                    ))}
                </ul>
            </div>
        </div>
    )
}


function link(type, node_name) {
    return '/'+ type + '/' + node_name
}

export default Gene