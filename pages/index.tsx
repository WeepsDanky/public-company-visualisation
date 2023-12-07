import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/link'
import { useRouter } from 'next/router'
import { useEffect, useRef } from 'react'


const Home: NextPage = ({ industryList }: { industryList : Array }) => {
  const router = useRouter()
  const { industryId: industryId } = router.query

  return (
    <>
      <Head>
        <title>The Industry | Company Visualisation</title>
        <meta
          property="og:image"
          content="https://public-company-visualisation.vercel.app/og-image.png"
        />
        <meta
          name="twitter:image"
          content="https://public-company-visualisation.vercel.app/og-image.png"
        />
      </Head>
      <main className="mx-auto max-w-[1960px] p-4">
        <div className="columns-1 gap-4 sm:columns-2 xl:columns-3 2xl:columns-4">
          <div className="after:content relative mb-5 flex h-[629px] flex-col items-center justify-end gap-4 overflow-hidden rounded-lg bg-white/10 px-3 pb-80 pt-64 text-center text-white shadow-highlight after:pointer-events-none after:absolute after:inset-0 after:rounded-lg after:shadow-highlight lg:pt-0">
            <h1 className="mt-3 mb-10 text-base font-bold tracking-widest">
              Summary of the Industry
            </h1>
            <ul className="max-w-[40ch] list-disc text-white/75 text-left sm:max-w-[32ch]">
              <li>This page can classify all public companies according to Global Industry Classification Standard (GICS), Bloomberg's Standard (BCS), or 申万行业分类 和 中信行业分类</li>
              <li>点进每一页查看行业具体信息</li>
            </ul>
          </div>

          {industryList.map(({ id, industry }) => (
            <Link
              key={industry}
              href={`/industry/${industry}`}
              className="after:content group relative mb-5 block w-full cursor-zoom-in after:pointer-events-none after:absolute after:inset-0 after:rounded-lg after:shadow-highlight"
            >
              <div className="max-w-md mx-auto rounded-xl shadow-md overflow-hidden md:max-w-2xl">
                <div className="p-8">
                  <div className="tracking-wide text-lg text-indigo-500 font-semibold">{industry}
                  </div>
                  <p className='text-white'> An explanation </p>
                </div>
              </div>
            </Link>
          ))}
        </div>
      </main>
      <footer className="p-6 text-center text-white/80 sm:p-12">
        Made by{' '}
       <a
          href="https://marksun.co.uk/"
          target="_blank"
          className="font-semibold hover:text-white"
          rel="noreferrer"
        >
          马克孙
        </a>
      </footer>
    </>
  )
}

export default Home

export async function getStaticProps() {

  const GICSList = ['Energy', 'Materials', 'Industrials', 'Consumer Discretionary', 'Consumer Staples', 'Health Care', 'Financials', 'Information Technology', 'Communication Services', 'Utilities', 'Real Estate']

  let industryList = []
  let i = 0
  for (let item of GICSList) { 
    industryList.push({
      id: i,
      industry: item,
    })
    i++
  }

  return {
    props: {
      industryList : industryList,
    },
  }
}
