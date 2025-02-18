local json = require("json")  -- Falls du dkjson verwendest
local socket = require("socket.http")

function recognizeSpeech()
    local url = "localhost:5000/recognize"
    local response, status = socket.request(url, "{}")

    if status == 200 then
        local data = json.decode(response)
        return data.recognized_text
    else
        return nil
    end
end

function parseATCCommand(command)
    command = string.lower(command)

    if string.match(command, "request landing") then
        return {type="LANDING_REQUEST", airport="Batumi"}
    elseif string.match(command, "cleared for takeoff") then
        return {type="TAKEOFF_CLEARANCE"}
    end

    return {type="UNKNOWN"}
end

-- Test
local speechText = recognizeSpeech()
if speechText then
    local parsedCommand = parseATCCommand(speechText)
    print("Parsed ATC Command:", parsedCommand.type)
end
