import { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import INfostering from '../components/Infostering'
import styles from '../styles/Home.module.css'

const Home: NextPage =() =>{
  return (
    <div className={styles.container}>
      <Head>
        <title>INfostering | Ai Generated Marketing</title>
        <meta name="description" content="Generate snippits for your" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <INfostering/>
    </div>
  )
}

export default Home;
