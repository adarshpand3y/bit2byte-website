import { useRouter } from 'next/router'
import Script from 'next/script'

const Blog = (props) => {
  const createMarkup = (c) => {
    return { __html: c };
  }

  return <>
    <Script
      strategy="afterInteractive"
      dangerouslySetInnerHTML={{
        __html: `
                Array.from(document.getElementsByTagName("h1")).forEach(item => item.classList.add("text-4xl"))
                Array.from(document.getElementsByTagName("h2")).forEach(item => item.classList.add("text-2xl"))
                Array.from(document.getElementsByTagName("h3")).forEach(item => item.classList.add("text-xl"))
                Array.from(document.getElementsByTagName("p")).forEach(item => item.classList.add("text-base"))
                Array.from(document.getElementsByTagName("ul")).forEach(item => item.classList.add("list-disc"))
                Array.from(document.getElementsByTagName("ol")).forEach(item => item.classList.add("list-decimal"))

  `,
      }}
    />
    <div className="container mx-auto my-2">
      <h1 className='text-4xl'>{props.parsedResponse.title}</h1>
      <div dangerouslySetInnerHTML={createMarkup(props.parsedResponse.body)}></div>
    </div>
  </>
}

export default Blog;

export async function getServerSideProps(context) {
  const slug = context.params.slug
  const url = `http://localhost:8000/api/getParticularBlog/${slug}`;
  const response = await fetch(url);
  const parsedResponse = await response.json();
  return {
    props: { parsedResponse }
  }
}