DROP PROCEDURE IF EXISTS 
IF EXISTS (SELECT * player_id, iglo.balance FROM iglo WHERE player_id=bjornar)  
	BEGIN 
		UPDATE iglo SET balance = (balance + 30) WHERE player_id=bjornar;
	END  
	
	ELSE
	BEGIN 
		INSERT INTO iglo (player_id, balance) VALUES (bjornar, 30); 
	END
