import React from 'react'
import Link from 'next/link';

const BlogItem = ({ details }) => {
    console.log(details);
    const timestamp = Date.parse(details.publish_date);
    const d = new Date(timestamp);
    return (
        <div className="-my-3 divide-y-2 divide-gray-100">
            <div className="py-8 flex flex-wrap md:flex-nowrap">
                <div className="md:w-64 md:mb-0 mb-6 flex-shrink-0 flex flex-col">
                    <span className="font-semibold title-font text-gray-700">{details.category}</span>
                    <span className="text-sm text-gray-500">{d.toLocaleDateString()}</span>
                </div>
                <div className="md:flex-grow">
                    <h2 className="text-2xl font-medium text-gray-900 title-font mb-2">{details.title}</h2>
                    <p className="leading-relaxed">{details.description}</p>
                    <Link href={`/blog/${details.slug}`}>
                        <a className="text-indigo-500 inline-flex items-center mt-4">Read More
                            <svg className="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2" fill="none" strokeLinecap="round" strokeLinejoin="round">
                                <path d="M5 12h14"></path>
                                <path d="M12 5l7 7-7 7"></path>
                            </svg>
                        </a>
                    </Link>
                </div>
            </div>
            <hr className='mb-3 mt-0' />
        </div>
    )
}

export default BlogItem;