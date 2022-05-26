import '../styles/globals.css'
import Navbar from '../Components/Navbar'
import Footer from '../Components/Footer'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function MyApp({ Component, pageProps }) {
  const showToast = (message, type) => {
    if(type == "error") toast.error(message);
    else if(type == "success") toast.success(message);
    else if(type == "info") toast.info(message);
    else toast.warning(message);
  }
  return (
    <>
      <Navbar />
      <ToastContainer
        position="bottom-center"
        autoClose={5000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
      />
      <Component {...pageProps} />
      <Footer showToast={showToast} />
    </>)
}

export default MyApp
