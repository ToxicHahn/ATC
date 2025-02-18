local json = require("json")  -- Falls du dkjson verwendest
local socket = require("socket.http")


local voskConn = {}
function voskConn.transcribe()
    local url = "192.168.188.69:5000/recognize"
    local response, status = socket.request(url, "{}")

    if status == 200 then
        print(status)
        local data = json.decode(response)
        return data.recognized_text
    else
        print(status)
        return nil
    end
end


