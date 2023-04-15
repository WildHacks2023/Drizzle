//
//  RunPythonScript.swift
//  testerfordrizzle
//
//  Created by Megha Pethari on 4/15/23.
//

import Foundation
import PythonKit

func RunPythonScript() -> PythonObject {
    let sys = Python.import("sys")
    sys.path.append("/Users/megha/Desktop/testerfordrizzle/testerfordrizzle/")
    let file = Python.import("OurPythonScript")
    
    let response = file.hello_world()
    print(response)
    return response
}




