
'use client'
import axios from "axios"
import React, { useState } from "react"

const tabs = ['Teacher Name', 'Subject', 'Fees', 'Duration', 'Username'];
export default  function  TeacherProfilePage() {

    const [currentTab, setCurrentTab] = useState(0)
    const [formData, setformData] = useState(
        {

            name:"",
            subject:"",
            fees:"",
            duration:"",
            username:""
        }
    )

    const progress =  ((currentTab) /  (tabs.length-1))*100
    const  handleTabClick =  async(index:number) => {
        setCurrentTab(index)
    }
    
    const  handleNext =  () =>  {
        if  ( currentTab <  tabs.length-1) {
            setCurrentTab(currentTab + 1)
        }
    }
    const  handlePrev=  () => {
        if (currentTab >   0){
            setCurrentTab(currentTab-1)
        }
    }
    const handleChange =  (e:React.ChangeEvent<HTMLInputElement>) =>  {
        setformData({...formData, [e.target.name]:e.target.value})
    }
    const  handleSubmit =  async() =>  {
        try {
            const  response =  await axios.post('http://127.0.0.1:8000/profile/create-teacher-profile/' , formData ,{
                withCredentials:true
            });
            alert('Profile created Successfully')
        } catch (error) {
            console.error(error);
            alert('Something went wrong!');
        }
    }

    const renderInputField = () =>  {
        const fields:  {[ key :  number] :  string} = {
            0: 'name',
            1: 'subject',
            2: 'fees',
            3: 'duration',
            4: 'username',
        }
    const fieldName =  fields[currentTab]
    return (
        <input 
        type="text"
        name={fieldName}
        value={(formData as any)[fieldName]}
        className="w-full p-4 border-b-2    text-black text-lg outline-none"
        placeholder={`Enter ${tabs[currentTab]}`}
        onChange={handleChange}
        />


    )

    }

    return (

        <div className="flex flex-col min-h-screen bg-gradient-to-br  bg-white">
            <div className="flex justify-center items-center border-b-2 border-gray-300 bg-[#003C6A] p-8 text-gray-100">
                {tabs.map((tab,index) =>  (
                    <button
                    key={index}
                    onClick={() =>  handleTabClick(index)}
                    className={`relative px-6 py-4 text-1xl font-normal transition-colors duration-300 uppercase hover:bg-[#0C487D] cursor-pointer ${
                        currentTab === index ? 'text-gray-300' : 'text-gray-200'
                      }`}
                    >
                        {tab}
                        {currentTab === index && (

              <span className="absolute left-0 bottom-0 w-full h-0.5 bg-blue-100 rounded-full animate-slide-in cursor-pointer"></span>

                        )}

                    </button>
                ))}

            </div>
            {/* progress bar  */}
            <div className="w-full  bg-gray-300 h-2">
            <div
                    className="bg-blue-600 h-2 transition-all duration-300"
                    style={{ width: `${progress}%` }}
                    />

            </div>

            <div className="flex flex-col items-center justify-center flex-grow p-8">
                    <div className="  w-full  max-w-2xl">
                        {renderInputField()}
                        <div className=" flex  justify-between  mt-10">
                            {currentTab >   0 && (
                                <button
                                onClick={handlePrev}
                                className="bg-gray-400 hover:bg-gray-500 text-white font-normal py-2 px-8 rounded cursor-pointer"

                                >
                                    Back 
                                </button>
                            )} 
                            {currentTab <  tabs.length - 1 ?   (

                                <button
                                onClick={handleNext}
                className="bg-blue-900  text-white font-normal py-2 px-8 rounded ml-auto cursor-pointer"

                                >
                                    Next 

                                </button>
                            ) :  (
                                <button
                                onClick={handleSubmit}
                                className="bg-blue-700 text-white font-normal py-2 px-8 rounded ml-auto cursor-pointer"

                                >
                                    Save
                                </button>
                            )}
                        </div>

                    </div>
            </div>
        </div>
    )


}