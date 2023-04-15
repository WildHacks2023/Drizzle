//
//  ContentView.swift
//  testerfordrizzle
//
//  Created by Megha Pethari on 4/15/23.
//

import SwiftUI

struct ContentView: View {
    //@State var countDownTimer = 5
    //@State var timerRunning = false
    //let timer = Timer.publish(every:1, on: .main, in: .common).autoconnect()
    @State var showResult: Bool = false
    var body: some View {
        VStack {
            Image(systemName: "person.circle.fill")
                .imageScale(.large)
                .foregroundColor(.accentColor)
            Text("Hello, Baby!")
        }
        .padding()
        
        Button(action: {
            RunPythonScript()
            showResult.toggle()
        }) {
            Text("Run Python Script")
        }
        if showResult {
            Text(String("\(RunPythonScript())"))
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
