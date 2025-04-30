
'use client'
import React from 'react'
import { useRouter } from 'next/navigation'
import Image from 'next/image'

const page = () => {
    const router =  useRouter()
  return (
    <main className=' bg-white  min-h-screen'>

        <h2 className=' text-black uppercase flex  items-center justify-center text-5xl  relative  top-10'>Choose Role  </h2>

    <div className=' flex  flex-row gap-10    items-center justify-around relative  top-20'>

        <div className='  flex  flex-col gap-5'>
            <Image
            src="/student.jpeg"
            height={300}
            width={300}
            alt='student'
            className=' cursor-pointer'
            />
        <button  className='  bg-blue-500   p-5  text-2xl cursor-pointer '
        onClick={() => router.push('/student') }
        >
            Student
        </button>
        <button
        onClick={() => router.push('/studentprofile')}
        className='  bg-blue-500   p-5  text-2xl cursor-pointer '
        >
            Your Profile
        </button>
        </div>
        <div className=' flex flex-col  gap-5'>
            <Image
            src="/teacher.jpg"
            height={300}
            width={300}
            alt='techer'
            className=' cursor-pointer'
            />
                    <button  className='  bg-blue-500   p-5  text-2xl cursor-pointer '
        onClick={() => router.push('/teacher') }
        >
            Teacher
        </button>
        </div>

    </div>
    </main>

  )
}

export default page