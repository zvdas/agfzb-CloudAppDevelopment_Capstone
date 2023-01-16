const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

function main(params) {

    const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY })
    const cloudant = CloudantV1.newInstance({
      authenticator: authenticator
    });
    cloudant.setServiceUrl(params.COUCH_URL);

    return getMatchingRecords(cloudant, "dealerships", params.SELECTOR);
}

 /*
 Sample implementation to get the records in a db based on a selector. If selector is empty, it returns all records. 
 eg: selector = {state:"Texas"} - Will return all records which has value 'Texas' in the column 'State'
 */
function getMatchingRecords(cloudant, dbname, selector) {
    return new Promise((resolve, reject) => {
        cloudant.postFind({db:dbname,selector:selector})
                .then((result)=>{
                  resolve({result:result.result.docs});
                })
                .catch(err => {
                   console.log(err);
                    reject({ err: err });
                });
         })
}


{
    "IAM_API_KEY": "vIu9HaKiRhjDxioRa24NhIKdxETRuWRJDhP8_fU9FWfc",
    "COUCH_URL": "https://b65d1bed-d060-4cb3-91b4-ba3cbb0b7e16-bluemix.cloudantnosqldb.appdomain.cloud",
    "SELECTOR": {"STATE": "California"}
}