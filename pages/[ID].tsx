import { useRouter } from 'next/router'

const Home = () => {
  const router = useRouter()
  const { id } = router.query

  console.log(id)

  return (
    <div>
      <h1>Industry: {industry}</h1>
    </div>
  )
}

export default Home
