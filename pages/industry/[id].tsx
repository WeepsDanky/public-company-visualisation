import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';

const Home = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const router = useRouter();
  const { id } = router.query; // get the ID from the URL

  useEffect(() => {
    const username = 'test-user'; // replace with your username
    const password = 'Pascal123'; // replace with your password
  
    // Create a base64 encoding of the username and password for basic auth
    const token = Buffer.from(`${username}:${password}`, 'utf8').toString('base64');
  
    fetch(`http://198.44.169.157:8000/api/companies/?IQ_SECTOR=${id}`, { // use the ID in the API call
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Basic ${token}`,
      },
    })
    .then((response: Response) => response.json())
    .then((data: any) => {
      setData(data);
      setLoading(false);
    })
    .catch((error: any) => {
      console.error('Error:', error);
    });
  }, [id]); // add id to the dependency array

  console.log(data);
// loading page
  if (loading) {
    return <div className="text-center text-white">
    <h1 className="text-4xl font-bold mb-4">Loading...</h1>
    <p className="opacity-75">Please wait, we're preparing something amazing for you!</p>
  </div>
  }

  return (
    <div className='flex flex-col items-center justify-center min-h-screen py-2'>
      <h1 className='text-white mono text-5xl border-4'>Industry</h1>
      <table className='text-white min-w-full divide-y divide-x divide-gray-200'>
        <thead>
          <tr>
            <th>SP_ENTITY_NAME</th>
            <th>SP_ENTITY_ID</th>
            <th>SP_EXCHANGE_TICKER</th>
            <th>IQ_INDUSTRY_CLASSIFICATION</th>
            <th>IQ_SECTOR</th>
            <th>IQ_INDUSTRY_GROUP</th>
            <th>IQ_INDUSTRY</th>
            <th>IQ_PRIMARY_INDUSTRY</th>
            <th>SP_GEOGRAPHY</th>
            <th>SP_COUNTRY_NAME</th>
          </tr>
        </thead>
        <tbody className='bg-slate-900 divide-y divide-gray-200'>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item.SP_ENTITY_NAME}</td>
              <td>{item.SP_ENTITY_ID}</td>
              <td>{item.SP_EXCHANGE_TICKER}</td>
              <td>{item.IQ_INDUSTRY_CLASSIFICATION}</td>
              <td>{item.IQ_SECTOR}</td>
              <td>{item.IQ_INDUSTRY_GROUP}</td>
              <td>{item.IQ_INDUSTRY}</td>
              <td>{item.IQ_PRIMARY_INDUSTRY}</td>
              <td>{item.SP_GEOGRAPHY}</td>
              <td>{item.SP_COUNTRY_NAME}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Home;