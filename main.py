from js import document

def calculateAverage(event):
    m_val = document.getElementById("math").value
    s_val = document.getElementById("science").value
    e_val = document.getElementById("english").value
    ss_val = document.getElementById("socialstudies").value
    res = document.getElementById("result")

    if not all([m_val, s_val, e_val, ss_val]):
        res.innerText = "Enter all grades."
        return

    try:
        math = int(m_val)
        science = int(s_val)
        english = int(e_val)
        socialstudies = int(ss_val)

        if (math < 1 or math > 100 or
            science < 1 or science > 100 or
            english < 1 or english > 100 or
            socialstudies < 1 or socialstudies > 100):
            
            res.innerText = "Invalid input. Use 1-100."
        
        else:
            GenAv = (math + science + english + socialstudies) / 4
            
            status = "Passed" if GenAv > 50 else "Failed"
            res.innerText = f"General Average: {GenAv}\n{status}"

    except ValueError:
        res.innerText = "Please enter valid numbers"