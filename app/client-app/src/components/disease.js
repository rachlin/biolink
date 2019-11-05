import React from 'react'

const Disease = ({disease}) => {
    
    var genes = [].concat(disease.AssociatedGenes)

    var related = Object.assign({}, disease.RelatedDiseases)
    var diseases = [].concat(related.RelatedByGene)

    return (
        <div>
            <center><h1>Disease {disease.DiseaseName} Details</h1></center>
            <div>
                Associated Genes
                <ul>
                    {genes.map((gene) => (
                        <li><a href={link("gene", gene)}>{gene}</a></li>
                    ))}
                </ul>
            </div>
            <div>
                Related Diseases by Gene Association
                <ul>
                    {diseases.map((disease) => (
                        <li><a href={link("disease", disease)}>{disease}</a></li>
                    ))}
                </ul>
            </div>
        </div>
    )
}


function link(type, node_name) {
    return '/'+ type + '/' + node_name
}

export default Disease