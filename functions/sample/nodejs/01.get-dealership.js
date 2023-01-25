const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

function main(params) {

    const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY })
    const cloudant = CloudantV1.newInstance({
      authenticator: authenticator
    });
    cloudant.setServiceUrl(params.COUCH_URL);

    return getAllRecords(cloudant, "dealerships");
}

 /*
 Sample implementation to get all the records in a db.
 */
 function getAllRecords(cloudant,dbname) {
     return new Promise((resolve, reject) => {
         cloudant.postAllDocs({ db: dbname, includeDocs: true })            
             .then((result)=>{
              console.log(result.result.rows)
              resolve({ result: result.result.rows });
             })
             .catch(err => {
                console.log(err);
                reject({ err: err });
             });
         })
 }
/*
{
    "IAM_API_KEY": "",
    "COUCH_URL": ""
}
*/
