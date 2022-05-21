import React from 'react';
import Link from 'next/link';
import BlogItem from '../Components/BlogItem';

const allblogs = (props) => {
    
    return (
        <>
            <section className="text-gray-600 body-font overflow-hidden">
                <div className="container px-5 py-2 mx-auto">
                    {
                        props.parsedResponse.map(item => <BlogItem key={item.id} details={item} />)
                    }
                    <h3 className='text-lg text-center p-4'>That's all we have for now</h3>
                </div>
            </section>
        </>
    )
}

export default allblogs;

export async function getServerSideProps(context) {
    const url = `http://localhost:8000/api/getblogs`;
      const response = await fetch(url);
      const parsedResponse = await response.json();
      console.log(parsedResponse);
    return {
      props: {parsedResponse}
    }
  }