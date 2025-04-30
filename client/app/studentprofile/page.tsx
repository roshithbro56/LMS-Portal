

'use client'
import axios from "axios"
import Cookies from "js-cookie"
import { useEffect, useState } from "react"

type  Profile = {
    name:string,
    email:string,
    gender:string,
    phone_number:string
}

export  default  function  ProfilePage() {

    const [profile, setProfile] = useState<Profile> ({
        name:"",
        email:"",
        gender:"",
        phone_number:""
    })
    const [message , setMessage ] = useState("")
    const [loading, setLoading] = useState(true)
    const [updating, setUpdating] = useState(false)

    const  fetchProfile =  async () =>  {
        setLoading(true)
        try {
            
            const token  =  Cookies.get('access')
            if  (!token){
                throw  new Error('Token  not  found  in   the Cookies')
            }
            const response =  await  axios.get<{student_profile:Profile}>
            ('http://127.0.0.1:8000/get-student-profile/' ,  {
                headers:{
                    Authorization:`Bearer ${token}`
                }
            })
            setProfile(response.data.student_profile)
            setLoading(false)
        } catch (error:any) {
            console.log(error)
            setMessage('Failed to  fetch  Student Profile')
        }
    }

    // update studnent content  
    const updateProfile =  async()=> {
        setUpdating(true)
        try {
            
            const token =  Cookies.get('access')
            if (!token){
                throw  new Error('No  token  found  in cookies')
            }
            const response  =  await  axios.post<{message:string}>
            ( 'http://127.0.0.1:8000/update-student-profile/',
                profile,
                {
                    headers:{
                        Authorization:`Bearer ${token}`
                    }
                }
            )
            setMessage(response.data.message)
            await  fetchProfile()
        } catch (error:any) {
            console.log(error)
            setMessage('Error updating the profile')
        } finally{
            setUpdating(false)
        }
    }

    useEffect(() => {
        fetchProfile()
    },[])
    useEffect(() =>  {
        if (message){
            const timer =  setTimeout(() =>  {
                setMessage('')
            },4000)

            return () => clearTimeout(timer)
        }
    },[message])

    // delete profile for the student 
    const deleteProfile =  async() =>  {
        const confirmed =  confirm("Are you sure you want to delete your profile? This action cannot be undone.")
        if (!confirmed) return

        try {
            const token =  Cookies.get('access')
            if (!token){
                throw  new Error('No  token  found')
            }
            const response  =  await  axios.delete<{message:string}>('http://127.0.0.1:8000/delete-student-profile/', {
                headers:{
                    Authorization :`Bearer ${token}`
                }
            })
            setMessage(response.data.message)
            Cookies.remove('access')

        } catch (error:any) {
            console.log(error)
            setMessage('Error deleting  Profile ')
        }
    }
    
    useEffect(() => {
        fetchProfile()
    },[])

    return (

        <div className=" flex  min-h-screen">
            <aside className="w-64 bg-gray-800 text-white p-6 hidden md:block">
            <h2 className="text-xl font-semibold mb-4">Dashboard</h2>
                <ul>
                <li className="mb-2">Profile</li>
                <li className="mb-2">Settings</li>
                </ul>
            </aside>

            <main className="flex-1 flex items-center justify-center">

                {message  &&   
                <p className=" mb-4 text-blue-800">
                    {message}
                </p>
                }
                {loading  ?   (
                    <p> Loading  ...</p>
                ) :  (

                    <form 
                    onSubmit={(e) =>  {
                        e.preventDefault()
                        updateProfile()
                    }}
                     className="grid grid-cols-1 gap-14  p-6 rounded-2xl shadow-xl"
                    >       
                            <div className=" flex flex-row gap-3">
                            <h2 className=" text-1xl  text-gray-300 uppercase mt-1 bg-[#333333] px-6 py-2 rounded-xl"> 
                                Name 
                            </h2>
                            <input 
                            type="text"
                            value={profile.name}
                            onChange={(e) => setProfile({...profile , name:e.target.value})}
                            placeholder="Name"
                            className="w-full p-2 border border-gray-600 rounded-2xl outline-none shadow-2xl ml-7  "
                            />

                            </div>

                            <div className=" flex flex-row  gap-3">
                            <h2 className=" text-1xl  text-gray-300 uppercase mt-1 bg-[#333333] px-6 py-2 rounded-xl"> 
                                Email 
                            </h2>
                            <input 
                            type="email"
                            value={profile.email}
                            onChange={(e) => setProfile({...profile,email:e.target.value})}
                            placeholder="email"
                            className="w-full p-2 border border-gray-600 rounded-2xl outline-none shadow-2xl ml-7 "
                            />
                            </div>
                            <div className=" flex flex-row  gap-3">
                            <h2 className=" text-1xl  text-gray-300 uppercase mt-1 bg-[#333333] px-6 py-2 rounded-xl"> 
                                Contact 
                            </h2>
                            <input 
                            type="text"
                            value={profile.phone_number}
                            onChange={(e) =>  setProfile({...profile ,  phone_number:e.target.value})}
                            placeholder="Phone Number"
                            className="w-full p-2 border border-gray-600 rounded-2xl outline-none shadow-2xl "
                            />
                            </div>
                            <div className=" flex flex-row  gap-3">
                            <h2 className=" text-1xl  text-gray-300 uppercase mt-1 bg-[#333333] px-6 py-2 rounded-xl"> 
                                Gender 
                            </h2>
                            <input 
                            type="text"
                            value={profile.gender}
                            onChange={(e) =>  setProfile({...profile ,  gender:e.target.value})}
                            placeholder="Gender"
                            className="w-full p-2 border border-gray-600 rounded-2xl outline-none shadow-2xl  ml-2"
                            />
                            </div>

                            <div className="col-span-2 flex justify-center">
  <button
    type="submit"
    className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 cursor-pointer"
    disabled={updating}
  >
    {updating ? 'Updating...' : 'Update Profile'}
  </button>
  <button
  type="button"
  onClick={deleteProfile}
  className="bg-[#333333] text-white px-6 py-2 rounded  ml-5 cursor-pointer"

  >
    Delete Profile
  </button>
</div>
                    </form>
                )}
            </main>
        </div>
    )
}